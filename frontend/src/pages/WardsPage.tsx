import { Button, Card, Form, Input, Table, Typography, message } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";

type Ward = { id: string; name: string };

export default function WardsPage() {
  const [wards, setWards] = useState<Ward[]>([]);
  const load = async () => setWards(await apiService.getWards() as Ward[]);
  useEffect(() => { void load(); }, []);

  const createWard = async (values: { name: string }) => {
    try { await apiService.createWard(values.name); await load(); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to create ward"); }
  };
  const assignNurse = async (values: { nurse_id: string; ward_id: string }) => {
    try { await apiService.assignNurse(values.nurse_id, values.ward_id); message.success("Ward nurse assigned"); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to assign nurse"); }
  };
  const assignPatient = async (values: { patient_id: string; ward_id: string; bed_room: string }) => {
    try { await apiService.assignPatientWard(values.patient_id, values.ward_id, values.bed_room); message.success("Patient assigned"); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to assign patient"); }
  };

  return (
    <Card>
      <Typography.Title level={2}>Wards</Typography.Title>
      <Form layout="inline" onFinish={createWard} style={{ marginBottom: 16 }}>
        <Form.Item name="name" rules={[{ required: true }]}><Input placeholder="Ward name" /></Form.Item>
        <Button htmlType="submit">Create ward</Button>
      </Form>
      <Form layout="inline" onFinish={assignNurse} style={{ marginBottom: 16 }}>
        <Form.Item name="nurse_id" rules={[{ required: true }]}><Input placeholder="Ward Nurse UUID" /></Form.Item>
        <Form.Item name="ward_id" rules={[{ required: true }]}><Input placeholder="Ward UUID" /></Form.Item>
        <Button htmlType="submit">Assign nurse</Button>
      </Form>
      <Form layout="inline" onFinish={assignPatient} style={{ marginBottom: 16 }}>
        <Form.Item name="patient_id" rules={[{ required: true }]}><Input placeholder="Patient UUID" /></Form.Item>
        <Form.Item name="ward_id" rules={[{ required: true }]}><Input placeholder="Ward UUID" /></Form.Item>
        <Form.Item name="bed_room" rules={[{ required: true }]}><Input placeholder="Bed/room" /></Form.Item>
        <Button type="primary" htmlType="submit">Assign patient</Button>
      </Form>
      <Table<Ward> rowKey="id" dataSource={wards} columns={[{ title: "Ward", dataIndex: "name" }, { title: "UUID", dataIndex: "id" }]} />
    </Card>
  );
}
