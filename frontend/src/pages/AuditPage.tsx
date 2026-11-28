import { Card, Table, Typography } from "antd";
import { useEffect, useState } from "react";
import { apiService } from "../services/api";

type Audit = { id: string; action: string; entity_type: string; actor_role: string; timestamp: string };

export default function AuditPage() {
  const [events, setEvents] = useState<Audit[]>([]);
  useEffect(() => { void apiService.getAudit().then((value) => setEvents(value as Audit[])); }, []);
  return (
    <Card>
      <Typography.Title level={2}>Audit log</Typography.Title>
      <Table<Audit> rowKey="id" dataSource={events} columns={[{ title: "Time", dataIndex: "timestamp" }, { title: "Action", dataIndex: "action" }, { title: "Entity", dataIndex: "entity_type" }, { title: "Role", dataIndex: "actor_role" }]} />
    </Card>
  );
}
