import { Button, Card, Form, Input, Typography, message } from "antd";
import { useState } from "react";
import { apiService } from "../services/api";

export default function PharmacyPage() {
  const [billCreated, setBillCreated] = useState(false);
  const create = async (values: { prescription_id: string }) => {
    try {
      const selected = [{ name: "Medicine 1", quantity: 1, unit_price: 50 }];
      await apiService.createMedicineBill(values.prescription_id, selected);
      setBillCreated(true);
      message.success("Medicine bill created");
    } catch (error) {
      message.error(error instanceof Error ? error.message : "Unable to create medicine bill");
    }
  };
  return (
    <Card>
      <Typography.Title level={2}>Pharmacy</Typography.Title>
      <Form layout="inline" onFinish={create} style={{ marginBottom: 16 }}>
        <Form.Item name="prescription_id" rules={[{ required: true }]}><Input placeholder="Prescription UUID" /></Form.Item>
        <Button htmlType="submit">Create Medicine 1 bill</Button>
      </Form>
      {billCreated && <Typography.Paragraph>Bill created with a demo Medicine 1 line.</Typography.Paragraph>}
    </Card>
  );
}
