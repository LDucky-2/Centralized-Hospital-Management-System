import { Navigate, Outlet } from "react-router";
import { useAuth } from "../context/AuthContext";

export function ITRoute() {
  const { account } = useAuth();
  if (account?.role !== "IT_ADMIN") return <Navigate to="/" replace />;
  return <Outlet />;
}
