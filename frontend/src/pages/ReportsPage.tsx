import { Button, Card, Form, Input, Table, Typography, message } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";

type Report = { id: string; patient_id: string; creator_id: string; near_future_message: string; created_at: string };

export default function ReportsPage() {
  const [reports, setReports] = useState<Report[]>([]);
  const load = async () => setReports(await apiService.getMedicalReports() as Report[]);
  useEffect(() => { void load(); }, []);
  const create = async (values: { patient_id: string }) => {
    try { await apiService.createMedicalReport(values.patient_id); message.success("Medical report placeholder created"); await load(); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to create report"); }
  };
  const external = async (values: { patient_id: string }) => {
    try { await apiService.createExternalReport(values.patient_id); message.success("External report placeholder created"); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to create external report"); }
  };
  return (
    <Card>
      <Typography.Title level={2}>Reports</Typography.Title>
      <Form layout="inline" onFinish={create} style={{ marginBottom: 16 }}>
        <Form.Item name="patient_id" rules={[{ required: true }]}><Input placeholder="Patient UUID" /></Form.Item>
        <Button htmlType="submit">Create medical placeholder</Button>
      </Form>
      <Form layout="inline" onFinish={external} style={{ marginBottom: 16 }}>
        <Form.Item name="patient_id" rules={[{ required: true }]}><Input placeholder="Patient UUID" /></Form.Item>
        <Button htmlType="submit">Create external placeholder</Button>
      </Form>
      <Table<Report> rowKey="id" dataSource={reports} columns={[{ title: "Patient", dataIndex: "patient_id" }, { title: "Status", dataIndex: "near_future_message" }]} />
    </Card>
  );
}
