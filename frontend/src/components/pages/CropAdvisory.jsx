import { useState } from "react";
import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Sprout, TrendingUp, Plus } from "lucide-react";

const CropAdvisory = () => {
  const [soilType, setSoilType] = useState("");
  const [region, setRegion] = useState("");
  const [season, setSeason] = useState("");

  const cropRecommendations = [
    {
      name: "Rice",
      image: "🌾",
      yield: "4.5 tons/hectare",
      demand: "High",
      demandTrend: "up",
    },
    {
      name: "Wheat",
      image: "🌾",
      yield: "3.8 tons/hectare",
      demand: "Medium",
      demandTrend: "stable",
    },
    {
      name: "Cotton",
      image: "🌿",
      yield: "2.2 tons/hectare",
      demand: "High",
      demandTrend: "up",
    },
    {
      name: "Sugarcane",
      image: "🎋",
      yield: "70 tons/hectare",
      demand: "Medium",
      demandTrend: "stable",
    },
  ];

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Navigation />
      
      <main className="flex-1 container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2 text-foreground">Crop Recommendation</h1>
          <p className="text-muted-foreground">Find the best crops for your farm based on conditions</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          {/* Filters */}
          <Card className="lg:col-span-1">
            <CardHeader>
              <CardTitle className="text-lg">Farm Details</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-2">
                <label className="text-sm font-medium">Soil Type</label>
                <Select value={soilType} onValueChange={setSoilType}>
                  <SelectTrigger>
                    <SelectValue placeholder="Select soil type" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="clay">Clay</SelectItem>
                    <SelectItem value="loamy">Loamy</SelectItem>
                    <SelectItem value="sandy">Sandy</SelectItem>
                    <SelectItem value="silt">Silt</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <label className="text-sm font-medium">Region</label>
                <Select value={region} onValueChange={setRegion}>
                  <SelectTrigger>
                    <SelectValue placeholder="Select region" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="north">North</SelectItem>
                    <SelectItem value="south">South</SelectItem>
                    <SelectItem value="east">East</SelectItem>
                    <SelectItem value="west">West</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <label className="text-sm font-medium">Season</label>
                <Select value={season} onValueChange={setSeason}>
                  <SelectTrigger>
                    <SelectValue placeholder="Select season" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="kharif">Kharif</SelectItem>
                    <SelectItem value="rabi">Rabi</SelectItem>
                    <SelectItem value="zaid">Zaid</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <Button className="w-full" disabled={!soilType || !region || !season}>
                Get Recommendations
              </Button>
            </CardContent>
          </Card>

          {/* Results */}
          <div className="lg:col-span-3">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {cropRecommendations.map((crop, index) => (
                <Card key={index} className="hover:shadow-lg transition-shadow">
                  <CardContent className="pt-6">
                    <div className="flex items-start gap-4">
                      <div className="text-4xl">{crop.image}</div>
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                          <h3 className="text-lg font-semibold">{crop.name}</h3>
                          <span className="text-sm text-muted-foreground">{crop.yield}</span>
                        </div>
                        
                        <div className="flex items-center gap-2 mb-4">
                          <span className="text-sm font-medium">Market Demand</span>
                          <span className={`px-2 py-1 rounded-full text-xs ${
                            crop.demand === "High" 
                              ? "bg-green-100 text-green-800" 
                              : "bg-yellow-100 text-yellow-800"
                          }`}>
                            {crop.demand}
                          </span>
                        </div>

                        <Button size="sm" className="gap-2">
                          <Plus className="h-4 w-4" />
                          Add to My Crop Plan
                        </Button>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default CropAdvisory;