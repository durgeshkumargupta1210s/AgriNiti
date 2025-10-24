import { useNavigate } from "react-router-dom";
import { BarChart3, Bug, Cloud, DollarSign, AlertTriangle, MessageSquare } from "lucide-react";
import FeatureCard from "@/components/FeatureCard";
import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";

const Dashboard = () => {
  const navigate = useNavigate();

  const features = [
    {
      icon: BarChart3,
      title: "Crop Recommendation",
      description: "Get personalized crop suggestions based on your soil type, region, and season.",
      path: "/crop-advisory",
    },
    {
      icon: Bug,
      title: "Pest & Disease Detection",
      description: "Upload images to identify pests and diseases with organic remedies.",
      path: "/pest-detection",
    },
    {
      icon: Cloud,
      title: "Weather Updates",
      description: "7-day weather forecast with live alerts for your region.",
      path: "/weather-market",
    },
    {
      icon: DollarSign,
      title: "Market Prices",
      description: "Real-time market prices for crops in your area.",
      path: "/weather-market",
    },
    {
      icon: AlertTriangle,
      title: "Alerts",
      description: "Important notifications about floods, pest outbreaks, and advisories.",
      path: "/",
    },
    {
      icon: MessageSquare,
      title: "Personalized Advisory",
      description: "Chat with our AI assistant for instant farming advice.",
      path: "/advisory",
    },
  ];

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Navigation />
      
      <main className="flex-1">
        {/* Hero Section */}
        <section className="bg-gradient-to-r from-primary to-primary-hover text-primary-foreground py-12">
          <div className="container mx-auto px-4">
            <h1 className="text-3xl md:text-4xl font-bold mb-2">Welcome, Farmer! 🌱</h1>
            <p className="text-lg opacity-90">Your smart farming companion for better yields</p>
          </div>
        </section>

        {/* Feature Cards Grid */}
        <section className="container mx-auto px-4 py-12">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((feature, index) => (
              <FeatureCard
                key={index}
                title={feature.title}
                icon={feature.icon}
                onClick={() => navigate(feature.path)}
              >
                <p className="text-muted-foreground text-sm">{feature.description}</p>
              </FeatureCard>
            ))}
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
};

export default Dashboard;
