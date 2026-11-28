import { Button, Card, Form, Input, Select, Table, Typography, message } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";

type Staff = { id: string; login_id: string; role: string; state: string };

const roles = [
  "DOCTOR", "WARD_DOCTOR", "ASSISTANT", "PATHOLOGIST", "ACCOUNTANT", "WARD_NURSE", "PHARMACY_STAFF", "IT_ADMIN",
];

export default function StaffPage() {
  const [staff, setStaff] = useState<Staff[]>([]);

  const load = async () => {
    try {
      setStaff(await apiService.getStaff() as Staff[]);
    } catch (error) {
      message.error(error instanceof Error ? error.message : "Unable to load staff");
    }
  };

  useEffect(() => { void load(); }, []);

  const create = async (values: { name: string; login_id: string; password: string; role: string }) => {
    try {
      await apiService.createStaff(values);
      message.success("Staff account created");
      await load();
    } catch (error) {
      message.error(error instanceof Error ? error.message : "Unable to create staff");
    }
  };

  const changeState = async (record: Staff, state: string) => {
    await apiService.updateStaff(record.id, { state });
    await load();
  };

  return (
    <Card>
      <Typography.Title level={2}>Staff administration</Typography.Title>
      <Form layout="inline" onFinish={create} style={{ marginBottom: 24, flexWrap: "wrap", gap: 8 }}>
        <Form.Item name="name" rules={[{ required: true }]}><Input placeholder="Name" /></Form.Item>
        <Form.Item name="login_id" rules={[{ required: true }]}><Input placeholder="4-digit ID" /></Form.Item>
        <Form.Item name="password" rules={[{ required: true }]}><Input.Password placeholder="Password" /></Form.Item>
        <Form.Item name="role" initialValue="DOCTOR"><Select options={roles.map((role) => ({ label: role, value: role }))} /></Form.Item>
        <Button type="primary" htmlType="submit">Create account</Button>
      </Form>
      <Table<Staff>
        rowKey="id"
        dataSource={staff}
        columns={[
          { title: "Login ID", dataIndex: "login_id" },
          { title: "Role", dataIndex: "role" },
          { title: "State", dataIndex: "state" },
          {
            title: "Action",
            render: (_, record) =>
              record.state === "ACTIVE"
                ? <Button danger onClick={() => void changeState(record, "BLOCKED")}>Block</Button>
                : <Button onClick={() => void changeState(record, "ACTIVE")}>Restore</Button>,
          },
        ]}
      />
    </Card>
  );
}
