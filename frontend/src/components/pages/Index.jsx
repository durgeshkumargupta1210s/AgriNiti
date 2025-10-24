import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Sprout, TrendingUp, Shield, Globe, LogIn, BarChart3, Bug, Cloud, MessageSquare } from "lucide-react";
import { useNavigate } from "react-router-dom";
import Footer from "@/components/Footer";

const Index = () => {
  const navigate = useNavigate();

  const features = [
    {
      icon: BarChart3,
      title: "AI-Powered Crop Recommendation",
      description: "Get personalized crop suggestions based on soil type, climate data, and market trends.",
    },
    {
      icon: Bug,
      title: "Pest & Disease Detection",
      description: "Upload crop images for instant pest identification with organic and chemical remedies.",
    },
    {
      icon: Cloud,
      title: "Weather & Market Updates",
      description: "Real-time weather alerts and mandi prices via IMD & e-NAM APIs.",
    },
    {
      icon: MessageSquare,
      title: "Multilingual AI Advisory",
      description: "Chat with our AI assistant in your preferred language for instant farming advice.",
    },
  ];

  const benefits = [
    {
      icon: TrendingUp,
      title: "Increase Income",
      description: "Data-driven decisions lead to better yields and higher profits.",
    },
    {
      icon: Shield,
      title: "Reduce Crop Loss",
      description: "Timely alerts and pest detection protect your harvests.",
    },
    {
      icon: Globe,
      title: "Accessible to All",
      description: "Multilingual support and simple interface for every farmer.",
    },
  ];

  return (
    <div className="min-h-screen bg-background flex flex-col">
      {/* Header */}
      <nav className="sticky top-0 z-50 bg-card border-b border-border shadow-sm">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-2 text-primary font-bold text-xl">
              <Sprout className="h-8 w-8" />
              <span>Smart Krishi</span>
            </div>
            <div className="flex items-center gap-3">
              <Button variant="ghost" size="sm" className="gap-2">
                <Globe className="h-4 w-4" />
                English
              </Button>
              <Button 
                variant="default" 
                size="sm"
                onClick={() => navigate('/login')}
                className="gap-2"
              >
                <LogIn className="h-4 w-4" />
                Login
              </Button>
            </div>
          </div>
        </div>
      </nav>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="bg-gradient-to-r from-primary to-primary-hover text-primary-foreground py-20">
          <div className="container mx-auto px-4 text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6 animate-fade-in">
              Smart Krishi 2025
            </h1>
            <p className="text-xl md:text-2xl mb-8 opacity-90">
              Empowering Farmers with AI-driven Decisions for Smarter Yields & Better Incomes
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Button 
                size="lg" 
                variant="secondary"
                className="text-lg px-8"
                onClick={() => navigate('/login')}
              >
                <LogIn className="mr-2 h-5 w-5" />
                Login / Sign Up
              </Button>
              <Button 
                size="lg" 
                variant="outline"
                className="text-lg px-8 bg-white/10 hover:bg-white/20 text-primary-foreground border-white/30"
                onClick={() => navigate('/dashboard')}
              >
                Explore Dashboard
              </Button>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl md:text-4xl font-bold mb-4 text-foreground">
                Comprehensive Farming Solutions
              </h2>
              <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
                End-to-end advisory system from crop planning to market selling
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {features.map((feature, index) => (
                <Card key={index} className="hover:shadow-lg transition-shadow">
                  <CardContent className="pt-6 text-center">
                    <div className="inline-flex items-center justify-center w-12 h-12 rounded-full bg-primary/10 mb-4">
                      <feature.icon className="h-6 w-6 text-primary" />
                    </div>
                    <h3 className="text-lg font-semibold mb-2 text-foreground">
                      {feature.title}
                    </h3>
                    <p className="text-sm text-muted-foreground">
                      {feature.description}
                    </p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Benefits Section */}
        <section className="py-16">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl md:text-4xl font-bold mb-4 text-foreground">
                Impact & Benefits
              </h2>
              <p className="text-lg text-muted-foreground">
                Making farming smarter, safer, and more profitable
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {benefits.map((benefit, index) => (
                <div key={index} className="text-center">
                  <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-accent/10 mb-4">
                    <benefit.icon className="h-8 w-8 text-accent" />
                  </div>
                  <h3 className="text-xl font-semibold mb-2 text-foreground">
                    {benefit.title}
                  </h3>
                  <p className="text-muted-foreground">
                    {benefit.description}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="py-16 bg-primary/5">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl md:text-4xl font-bold mb-4 text-foreground">
              Ready to Transform Your Farming?
            </h2>
            <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
              Join thousands of farmers already using Smart Krishi to boost yields and income
            </p>
            <Button 
              size="lg" 
              className="text-lg px-8"
              onClick={() => navigate('/login')}
            >
              Get Started Free
            </Button>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
};

export default Index;
