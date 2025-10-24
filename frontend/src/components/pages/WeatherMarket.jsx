import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Cloud, DollarSign, TrendingUp, MapPin, Calendar } from "lucide-react";

const WeatherMarket = () => {
  const weatherData = [
    { day: "Today", temp: "32°C", condition: "Sunny", humidity: "65%", wind: "12 km/h" },
    { day: "Tomorrow", temp: "28°C", condition: "Partly Cloudy", humidity: "70%", wind: "8 km/h" },
    { day: "Day 3", temp: "30°C", condition: "Clear", humidity: "60%", wind: "15 km/h" },
    { day: "Day 4", temp: "26°C", condition: "Rain", humidity: "85%", wind: "20 km/h" },
    { day: "Day 5", temp: "29°C", condition: "Cloudy", humidity: "75%", wind: "10 km/h" },
  ];

  const marketPrices = [
    { crop: "Rice", price: "₹2,850", change: "+5.2%", trend: "up" },
    { crop: "Wheat", price: "₹2,200", change: "+2.1%", trend: "up" },
    { crop: "Cotton", price: "₹6,500", change: "-1.8%", trend: "down" },
    { crop: "Sugarcane", price: "₹3,200", change: "+3.5%", trend: "up" },
    { crop: "Soybean", price: "₹4,100", change: "-0.5%", trend: "down" },
  ];

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Navigation />
      
      <main className="flex-1 container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2 text-foreground">Weather & Market</h1>
          <p className="text-muted-foreground">Real-time weather updates and market prices</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Weather Section */}
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Cloud className="h-5 w-5 text-primary" />
                <CardTitle>7-Day Weather Forecast</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {weatherData.map((day, index) => (
                  <div key={index} className="flex items-center justify-between p-3 rounded-lg bg-muted">
                    <div className="flex items-center gap-3">
                      <div className="text-sm font-medium">{day.day}</div>
                      <div className="text-2xl font-bold">{day.temp}</div>
                    </div>
                    <div className="text-right">
                      <div className="text-sm text-muted-foreground">{day.condition}</div>
                      <div className="text-xs text-muted-foreground">
                        Humidity: {day.humidity} | Wind: {day.wind}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Market Prices Section */}
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <DollarSign className="h-5 w-5 text-primary" />
                <CardTitle>Market Prices</CardTitle>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {marketPrices.map((crop, index) => (
                  <div key={index} className="flex items-center justify-between p-3 rounded-lg bg-muted">
                    <div>
                      <div className="font-medium">{crop.crop}</div>
                      <div className="text-sm text-muted-foreground">Per Quintal</div>
                    </div>
                    <div className="text-right">
                      <div className="font-bold">{crop.price}</div>
                      <Badge 
                        variant={crop.trend === "up" ? "default" : "destructive"}
                        className="text-xs"
                      >
                        {crop.change}
                      </Badge>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Alerts Section */}
        <Card className="mt-6">
          <CardHeader>
            <div className="flex items-center gap-2">
              <Calendar className="h-5 w-5 text-primary" />
              <CardTitle>Weather Alerts</CardTitle>
            </div>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              <div className="p-3 rounded-lg bg-yellow-50 border border-yellow-200">
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-yellow-500 rounded-full"></div>
                  <span className="font-medium text-yellow-800">Rain Alert</span>
                </div>
                <p className="text-sm text-yellow-700 mt-1">
                  Heavy rainfall expected in the next 2 days. Take necessary precautions for your crops.
                </p>
              </div>
              
              <div className="p-3 rounded-lg bg-green-50 border border-green-200">
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                  <span className="font-medium text-green-800">Good Weather</span>
                </div>
                <p className="text-sm text-green-700 mt-1">
                  Perfect conditions for crop growth. Ideal time for planting activities.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </main>

      <Footer />
    </div>
  );
};

export default WeatherMarket;
