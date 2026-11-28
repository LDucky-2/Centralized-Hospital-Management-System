import { Button, Card, Form, Input, Select, Table, Typography, message } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";
import { useAuth } from "../context/AuthContext";

type Appointment = { id: string; patient_id: string; doctor_id: string; appointment_date: string; start_time: string; status: string };
type Doctor = { id: string; name: string; login_id: string };

export default function AppointmentsPage() {
  const { account } = useAuth();
  const [appointments, setAppointments] = useState<Appointment[]>([]);
  const [doctors, setDoctors] = useState<Doctor[]>([]);
  const [slots, setSlots] = useState<string[]>([]);
  const [selectedDoctor, setSelectedDoctor] = useState<string>("");
  const [date, setDate] = useState(new Date().toISOString().slice(0, 10));

  const load = async () => {
    if (!account) return;
    try {
      if (account.role === "PATIENT") {
        setAppointments(await apiService.getMyAppointments() as Appointment[]);
        setDoctors(await apiService.getDoctors() as Doctor[]);
        if (selectedDoctor) {
          setSlots(await apiService.getAvailableSlots(selectedDoctor, date) as string[]);
        }
      } else {
        setAppointments(await apiService.getAppointments(account.id, date) as Appointment[]);
      }
    } catch (error) {
      message.error(error instanceof Error ? error.message : "Unable to load appointments");
    }
  };

  useEffect(() => { void load(); }, [account, date, selectedDoctor]);

  const create = async (values: { patient_id: string; doctor_id: string; start_time: string }) => {
    try {
      await apiService.createAppointment(
        account?.role === "PATIENT"
          ? { doctor_id: selectedDoctor, start_time: values.start_time, appointment_date: date }
          : { ...values, appointment_date: date },
      );
      message.success("Appointment booked");
      await load();
    } catch (error) {
      message.error(error instanceof Error ? error.message : "Unable to book appointment");
    }
  };

  return (
    <Card>
      <Typography.Title level={2}>Appointments</Typography.Title>
      <Input type="date" value={date} onChange={(event) => setDate(event.target.value)} style={{ maxWidth: 220, marginBottom: 16 }} />
      {account?.role === "PATIENT" ? (
        <Form layout="inline" onFinish={create} style={{ margin: "16px 0", flexWrap: "wrap" }}>
          <Form.Item label="Doctor" required>
            <Select
              style={{ width: 220 }}
              value={selectedDoctor || undefined}
              placeholder="Select Doctor"
              options={doctors.map((doctor) => ({ label: doctor.name, value: doctor.id }))}
              onChange={(value) => setSelectedDoctor(value)}
            />
          </Form.Item>
          <Form.Item name="start_time" label="Time" rules={[{ required: true }]}>
            <Select style={{ width: 180 }} placeholder="Select 15-minute slot" options={slots.map((slot) => ({ label: slot, value: slot }))} />
          </Form.Item>
          <Button type="primary" htmlType="submit" disabled={!selectedDoctor}>Book</Button>
        </Form>
      ) : (
        <Form layout="inline" onFinish={create} style={{ margin: "16px 0", flexWrap: "wrap" }}>
          <Form.Item name="patient_id" rules={[{ required: true }]}><Input placeholder="Patient UUID" /></Form.Item>
          <Form.Item name="doctor_id" initialValue={account?.role === "DOCTOR" ? account.id : undefined} rules={[{ required: true }]}><Input placeholder="Doctor UUID" /></Form.Item>
          <Form.Item name="start_time" rules={[{ required: true }]}><Input placeholder="15-minute time, e.g. 09:00" /></Form.Item>
          <Button type="primary" htmlType="submit">Book</Button>
        </Form>
      )}
      <Table<Appointment>
        rowKey="id"
        dataSource={appointments}
        columns={[
          { title: "Patient", dataIndex: "patient_id" },
          { title: "Time", dataIndex: "start_time" },
          { title: "Status", dataIndex: "status" },
          { title: "Action", render: (_, record) => (
            <Button danger disabled={record.status !== "SCHEDULED"} onClick={async () => {
              try { await apiService.cancelAppointment(record.id); await load(); } catch (error) { message.error(error instanceof Error ? error.message : "Unable to cancel"); }
            }}>Cancel</Button>
          ) },
        ]}
      />
    </Card>
  );
}
