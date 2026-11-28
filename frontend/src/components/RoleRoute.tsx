import { Navigate, Outlet } from "react-router";
import { useAuth } from "../context/AuthContext";
import type { AccountRole } from "../types/auth";

export function RoleRoute({ allowed }: { allowed: AccountRole[] }) {
  const { account } = useAuth();
  if (!account || !allowed.includes(account.role)) return <Navigate to="/" replace />;
  return <Outlet />;
}
