import { useState } from "react";
import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Upload, Camera, Leaf } from "lucide-react";

const PestDetection = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [detectionResult, setDetectionResult] = useState(false);

  const handleImageUpload = (event) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setSelectedImage(reader.result);
        // Simulate detection after 1 second
        setTimeout(() => setDetectionResult(true), 1000);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Navigation />
      
      <main className="flex-1 container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2 text-foreground">Pest & Disease Detection</h1>
          <p className="text-muted-foreground">Upload or capture images to identify crop issues</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Upload Section */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Upload className="h-5 w-5 text-primary" />
                Upload Image
              </CardTitle>
            </CardHeader>
            <CardContent>
              {selectedImage ? (
                <div className="space-y-4">
                  <img
                    src={selectedImage}
                    alt="Uploaded"
                    className="w-full h-64 object-cover rounded-lg"
                  />
                  <Button onClick={() => setSelectedImage(null)} variant="outline">
                    Remove Image
                  </Button>
                </div>
              ) : (
                <div className="border-2 border-dashed border-muted-foreground/25 rounded-lg p-8 text-center">
                  <Leaf className="h-12 w-12 mx-auto mb-4 text-muted-foreground" />
                  <p className="text-muted-foreground mb-4">
                    Drag and drop an image or click to browse
                  </p>
                  <input
                    type="file"
                    accept="image/*"
                    onChange={handleImageUpload}
                    className="hidden"
                    id="image-upload"
                  />
                  <label htmlFor="image-upload">
                    <Button asChild>
                      <span>Upload Image</span>
                    </Button>
                  </label>
                </div>
              )}
            </CardContent>
          </Card>

          {/* Results Section */}
          <Card>
            <CardHeader>
              <CardTitle>Detection Results</CardTitle>
            </CardHeader>
            <CardContent>
              {!detectionResult ? (
                <div className="text-center py-8 text-muted-foreground">
                  Upload an image to see detection results
                </div>
              ) : (
                <div className="space-y-4">
                  <div className="p-4 bg-destructive/10 border border-destructive/20 rounded-lg">
                    <h3 className="font-semibold text-destructive">Detected: Leaf Blight</h3>
                    <p className="text-sm text-muted-foreground mt-1">
                      Fungal disease affecting crop leaves
                    </p>
                  </div>

                  <Tabs defaultValue="organic" className="w-full">
                    <TabsList className="grid w-full grid-cols-3">
                      <TabsTrigger value="organic">Organic</TabsTrigger>
                      <TabsTrigger value="chemical">Chemical</TabsTrigger>
                      <TabsTrigger value="preventive">Preventive</TabsTrigger>
                    </TabsList>

                    <TabsContent value="organic" className="space-y-3">
                      <div className="p-3 border rounded-lg">
                        <h4 className="font-medium">Neem Oil Spray</h4>
                        <p className="text-sm text-muted-foreground mt-1">
                          Mix 5ml neem oil per liter of water. Spray in the evening.
                        </p>
                      </div>
                      <div className="p-3 border rounded-lg">
                        <h4 className="font-medium">Garlic Extract</h4>
                        <p className="text-sm text-muted-foreground mt-1">
                          Crush 100g garlic in 1L water. Strain and spray on affected areas.
                        </p>
                      </div>
                    </TabsContent>

                    <TabsContent value="chemical" className="space-y-3">
                      <div className="p-3 border rounded-lg">
                        <h4 className="font-medium">Copper Fungicide</h4>
                        <p className="text-sm text-muted-foreground mt-1">
                          Apply as per manufacturer instructions. Use protective equipment.
                        </p>
                      </div>
                    </TabsContent>

                    <TabsContent value="preventive" className="space-y-3">
                      <div className="p-3 border rounded-lg">
                        <h4 className="font-medium">Crop Rotation</h4>
                        <p className="text-sm text-muted-foreground mt-1">
                          Rotate with non-host crops to break disease cycle.
                        </p>
                      </div>
                      <div className="p-3 border rounded-lg">
                        <h4 className="font-medium">Proper Drainage</h4>
                        <p className="text-sm text-muted-foreground mt-1">
                          Ensure good field drainage to prevent fungal growth.
                        </p>
                      </div>
                    </TabsContent>
                  </Tabs>
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default PestDetection;