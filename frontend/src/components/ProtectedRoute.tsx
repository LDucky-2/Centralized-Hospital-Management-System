import { Spin } from "antd";
import { Navigate, Outlet, useLocation } from "react-router";
import { useAuth } from "../context/AuthContext";

export function ProtectedRoute() {
  const { account, loading } = useAuth();
  const location = useLocation();
  if (loading) return <Spin size="large" style={{ display: "block", margin: "64px auto" }} />;
  if (!account) return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  return <Outlet />;
}
