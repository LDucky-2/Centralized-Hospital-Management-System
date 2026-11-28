import { Button, Card, Form, Input, Table, Typography, message } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";

type Bill = { id: string; patient_id: string; line_items: unknown[]; total: number; status: string };

export default function BillingPage() {
  const [bills, setBills] = useState<Bill[]>([]);
  const load = async () => setBills(await apiService.getBills() as Bill[]);
  useEffect(() => { void load(); }, []);

  const create = async (values: { patient_id: string }) => {
    try { await apiService.createBill(values.patient_id, [{ name: "Placeholder Test 1", quantity: 1, unit_price: 500 }]); message.success("Bill created"); await load(); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to create bill"); }
  };

  return (
    <Card>
      <Typography.Title level={2}>Billing</Typography.Title>
      <Form layout="inline" onFinish={create} style={{ marginBottom: 16 }}>
        <Form.Item name="patient_id" rules={[{ required: true }]}><Input placeholder="Patient UUID" /></Form.Item>
        <Button htmlType="submit">Create test bill</Button>
      </Form>
      <Table<Bill> rowKey="id" dataSource={bills} columns={[
        { title: "Patient", dataIndex: "patient_id" }, { title: "Total", dataIndex: "total" }, { title: "Status", dataIndex: "status" },
        { title: "Action", render: (_, bill) => bill.status === "UNPAID" ? <Button onClick={async () => { try { await apiService.markBillPaid(bill.id); await load(); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to mark paid"); } }}>Mark paid</Button> : null },
      ]} />
    </Card>
  );
}
