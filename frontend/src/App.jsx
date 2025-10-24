import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Index from "./components/pages/Index";
import Login from "./components/pages/Login";
import Dashboard from "./components/pages/Dashboard";
import CropAdvisory from "./components/pages/CropAdvisory";
import PestDetection from "./components/pages/PestDetection";
import WeatherMarket from "./components/pages/WeatherMarket";
import Forum from "./components/pages/Forum";
import Advisory from "./components/pages/Advisory";
import Profile from "./components/pages/Profile";
import NotFound from "./components/pages/NotFound";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Index />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/crop-advisory" element={<CropAdvisory />} />
          <Route path="/pest-detection" element={<PestDetection />} />
          <Route path="/weather-market" element={<WeatherMarket />} />
          <Route path="/forum" element={<Forum />} />
          <Route path="/advisory" element={<Advisory />} />
          <Route path="/profile" element={<Profile />} />
          {/* ADD ALL CUSTOM ROUTES ABOVE THE CATCH-ALL "*" ROUTE */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;
