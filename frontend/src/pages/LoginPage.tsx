import { Button, Card, Form, Input, Typography, message } from "antd";
import { Link, useNavigate } from "react-router";
import { useAuth } from "../context/AuthContext";

export default function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const submit = async (values: { login_id: string; password: string }) => {
    try {
      await login(values);
      navigate("/");
    } catch (error) {
      message.error(error instanceof Error ? error.message : "Login failed");
    }
  };

  return (
    <Card style={{ maxWidth: 420, margin: "48px auto" }}>
      <Typography.Title level={2}>CHMS</Typography.Title>
      <Typography.Paragraph>Centralized Hospital Management System</Typography.Paragraph>
      <Form layout="vertical" onFinish={submit}>
        <Form.Item name="login_id" label="Patient or Staff ID" rules={[{ required: true }]}>
          <Input />
        </Form.Item>
        <Form.Item name="password" label="Password" rules={[{ required: true }]}>
          <Input.Password />
        </Form.Item>
        <Button type="primary" htmlType="submit" block>Log in</Button>
      </Form>
      <Typography.Paragraph style={{ marginTop: 16 }}>
        <Link to="/register">Create patient account</Link>
      </Typography.Paragraph>
    </Card>
  );
}
