import { Button, Card, Form, Input, Table, Typography, message } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";

type Prescription = { id: string; patient_id: string; creator_id: string; near_future_message: string; created_at: string };

export default function PrescriptionsPage() {
  const [prescriptions, setPrescriptions] = useState<Prescription[]>([]);
  const load = async () => setPrescriptions(await apiService.getPrescriptions() as Prescription[]);
  useEffect(() => { void load(); }, []);
  const create = async (values: { patient_id: string }) => {
    try { await apiService.createPrescription(values.patient_id); message.success("Prescription placeholder created"); await load(); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to create prescription"); }
  };
  return (
    <Card>
      <Typography.Title level={2}>Prescriptions</Typography.Title>
      <Form layout="inline" onFinish={create} style={{ marginBottom: 16 }}>
        <Form.Item name="patient_id" rules={[{ required: true }]}><Input placeholder="Patient UUID" /></Form.Item>
        <Button htmlType="submit">Create placeholder</Button>
      </Form>
      <Table<Prescription> rowKey="id" dataSource={prescriptions} columns={[
        { title: "Patient", dataIndex: "patient_id" }, { title: "Created", dataIndex: "created_at" },
        { title: "Status", dataIndex: "near_future_message" },
      ]} />
    </Card>
  );
}
