import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { MapPin, Sprout, MessageSquare, Settings, Globe, Bell } from "lucide-react";
import { Switch } from "@/components/ui/switch";

const Profile = () => {
  const savedCrops = [
    { name: "Rice", season: "Kharif", status: "Active" },
    { name: "Wheat", season: "Rabi", status: "Planned" },
    { name: "Cotton", season: "Kharif", status: "Completed" },
  ];

  const recentAdvisories = [
    { date: "2 days ago", topic: "Pest control for wheat", type: "Pest Management" },
    { date: "1 week ago", topic: "Fertilizer recommendations", type: "Crop Care" },
    { date: "2 weeks ago", topic: "Market price inquiry", type: "Market Info" },
  ];

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Navigation />
      
      <main className="flex-1 container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2 text-foreground">My Profile</h1>
          <p className="text-muted-foreground">Manage your account and preferences</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Profile Card */}
          <Card className="lg:col-span-1">
            <CardContent className="pt-6">
              <div className="flex flex-col items-center text-center space-y-4">
                <Avatar className="h-24 w-24">
                  <AvatarFallback className="bg-primary text-primary-foreground text-2xl">
                    RK
                  </AvatarFallback>
                </Avatar>
                <div>
                  <h2 className="text-xl font-bold">Rajesh Kumar</h2>
                  <div className="flex items-center justify-center gap-1 text-muted-foreground mt-1">
                    <MapPin className="h-4 w-4" />
                    <span className="text-sm">Punjab, India</span>
                  </div>
                </div>
                <div className="flex gap-2">
                  <Badge variant="secondary">Premium Member</Badge>
                </div>
                <Button variant="outline" className="w-full gap-2">
                  <Settings className="h-4 w-4" />
                  Edit Profile
                </Button>
              </div>
            </CardContent>
          </Card>

          {/* Main Content */}
          <div className="lg:col-span-2 space-y-6">
            {/* Saved Crops */}
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <Sprout className="h-5 w-5 text-primary" />
                  <CardTitle>My Crop Plan</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {savedCrops.map((crop, index) => (
                    <div
                      key={index}
                      className="flex items-center justify-between p-3 rounded-lg bg-muted"
                    >
                      <div>
                        <p className="font-medium">{crop.name}</p>
                        <p className="text-sm text-muted-foreground">{crop.season} Season</p>
                      </div>
                      <Badge
                        variant={
                          crop.status === "Active"
                            ? "default"
                            : crop.status === "Planned"
                            ? "secondary"
                            : "outline"
                        }
                      >
                        {crop.status}
                      </Badge>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Advisory History */}
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <MessageSquare className="h-5 w-5 text-primary" />
                  <CardTitle>Recent Advisory</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {recentAdvisories.map((advisory, index) => (
                    <div
                      key={index}
                      className="flex items-start justify-between p-3 rounded-lg bg-muted hover:bg-muted/80 cursor-pointer transition-colors"
                    >
                      <div className="flex-1">
                        <p className="font-medium text-sm">{advisory.topic}</p>
                        <p className="text-xs text-muted-foreground mt-1">{advisory.type}</p>
                      </div>
                      <span className="text-xs text-muted-foreground">{advisory.date}</span>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Settings */}
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <Settings className="h-5 w-5 text-primary" />
                  <CardTitle>Preferences</CardTitle>
                </div>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Globe className="h-4 w-4 text-muted-foreground" />
                    <span className="text-sm font-medium">Language</span>
                  </div>
                  <Button variant="outline" size="sm">
                    English
                  </Button>
                </div>
                
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Bell className="h-4 w-4 text-muted-foreground" />
                    <span className="text-sm font-medium">Notifications</span>
                  </div>
                  <Switch defaultChecked />
                </div>
                
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Sprout className="h-4 w-4 text-muted-foreground" />
                    <span className="text-sm font-medium">Offline Mode</span>
                  </div>
                  <Switch />
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default Profile;
