import { Button, Card, Form, Input, Select, Table, Typography, message } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";

type Pathology = { id: string; patient_id: string; test_name: string; billing_status: string; publish_date: string; near_future_message: string };

export default function PathologyPage() {
  const [reports, setReports] = useState<Pathology[]>([]);
  const load = async () => setReports(await apiService.getPathology() as Pathology[]);
  useEffect(() => { void load(); }, []);
  const create = async (values: { patient_id: string; test_name: string; billing_status: string }) => {
    try { await apiService.createPathology(values.patient_id, values.test_name, values.billing_status); message.success("Pathology placeholder published"); await load(); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to publish pathology placeholder"); }
  };
  return (
    <Card>
      <Typography.Title level={2}>Pathology</Typography.Title>
      <Form layout="inline" onFinish={create} style={{ marginBottom: 16 }}>
        <Form.Item name="patient_id" rules={[{ required: true }]}><Input placeholder="Patient UUID" /></Form.Item>
        <Form.Item name="test_name" rules={[{ required: true }]}><Input placeholder="Placeholder Test 1" /></Form.Item>
        <Form.Item name="billing_status" initialValue="UNPAID"><Select options={[{ label: "Unpaid", value: "UNPAID" }, { label: "Paid", value: "PAID" }]} /></Form.Item>
        <Button htmlType="submit">Publish placeholder</Button>
      </Form>
      <Table<Pathology> rowKey="id" dataSource={reports} columns={[{ title: "Patient", dataIndex: "patient_id" }, { title: "Test", dataIndex: "test_name" }, { title: "Billing", dataIndex: "billing_status" }, { title: "Status", dataIndex: "near_future_message" }]} />
    </Card>
  );
}
