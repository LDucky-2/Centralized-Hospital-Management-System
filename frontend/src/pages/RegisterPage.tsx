import { Button, Card, Form, Input, Typography, message } from "antd";
import { apiService } from "../services/api";

export default function RegisterPage() {
  const submit = async (values: Record<string, string>) => {
    try {
      const result = await apiService.registerPatient({
        ...values,
        blood_group: values.blood_group || null,
      }) as { patient_id: string };
      message.success(`Account created. Patient ID: ${result.patient_id}`);
    } catch (error) {
      message.error(error instanceof Error ? error.message : "Registration failed");
    }
  };

  return (
    <Card style={{ maxWidth: 680, margin: "32px auto" }}>
      <Typography.Title level={2}>Patient registration</Typography.Title>
      <Form layout="vertical" onFinish={submit}>
        <Form.Item name="name" label="Name" rules={[{ required: true }]}><Input /></Form.Item>
        <Form.Item name="phone" label="Phone" rules={[{ required: true }]}><Input /></Form.Item>
        <Form.Item name="address" label="Address" rules={[{ required: true }]}><Input /></Form.Item>
        <Form.Item name="date_of_birth" label="Date of birth" rules={[{ required: true }]}><Input type="date" /></Form.Item>
        <Form.Item name="emergency_contact" label="Emergency contact" rules={[{ required: true }]}><Input /></Form.Item>
        <Form.Item name="password" label="Password" rules={[{ required: true }]}><Input.Password /></Form.Item>
        <Form.Item name="blood_group" label="Blood group (optional)"><Input /></Form.Item>
        <Button type="primary" htmlType="submit">Register</Button>
      </Form>
    </Card>
  );
}
