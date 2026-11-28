import { createContext, useContext, useEffect, useState, type ReactNode } from "react";
import { apiService } from "../services/api";
import type { Account, LoginInput } from "../types/auth";

type AuthContextValue = {
  account: Account | null;
  loading: boolean;
  login: (data: LoginInput) => Promise<void>;
  logout: () => Promise<void>;
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [account, setAccount] = useState<Account | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    apiService.onSessionExpired(() => setAccount(null));
    apiService.restoreSession().then(setAccount).finally(() => setLoading(false));
    return () => apiService.onSessionExpired(null);
  }, []);

  const login = async (data: LoginInput) => {
    await apiService.login(data);
    setAccount(await apiService.getMe());
  };

  const logout = async () => {
    try {
      await apiService.logout();
    } finally {
      setAccount(null);
    }
  };

  return (
    <AuthContext.Provider value={{ account, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used inside AuthProvider");
  return context;
}
