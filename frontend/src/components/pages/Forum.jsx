import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Heart, MessageCircle, Share2, TrendingUp } from "lucide-react";

const Forum = () => {
  const posts = [
    {
      author: "Rajesh Kumar",
      avatar: "RK",
      time: "2 hours ago",
      content: "Best practices for pest control in wheat crops during winter season? Looking for organic solutions.",
      likes: 12,
      comments: 5,
    },
    {
      author: "Priya Sharma",
      avatar: "PS",
      time: "5 hours ago",
      content: "Successfully implemented drip irrigation in my cotton farm. Water usage reduced by 40%! Happy to share my experience.",
      likes: 8,
      comments: 3,
    },
    {
      author: "Amit Patel",
      avatar: "AP",
      time: "1 day ago",
      content: "Market prices for rice are looking good this month. Anyone planning to sell their harvest soon?",
      likes: 15,
      comments: 7,
    },
  ];

  const trendingTopics = [
    "Organic Farming",
    "Drip Irrigation",
    "Rice Market Prices",
    "Pest Control",
    "Monsoon Preparation",
  ];

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Navigation />
      
      <main className="flex-1 container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2 text-foreground">Community Forum</h1>
          <p className="text-muted-foreground">Connect with fellow farmers and share experiences</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Main Feed */}
          <div className="lg:col-span-2 space-y-6">
            {/* Create Post */}
            <Card>
              <CardContent className="pt-6">
                <div className="flex gap-3">
                  <Avatar>
                    <AvatarFallback>U</AvatarFallback>
                  </Avatar>
                  <div className="flex-1">
                    <Textarea
                      placeholder="Share your farming experience, ask questions, or start a discussion..."
                      className="min-h-[100px] resize-none"
                    />
                    <div className="flex justify-end mt-3">
                      <Button>Post</Button>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Posts Feed */}
            {posts.map((post, index) => (
              <Card key={index}>
                <CardContent className="pt-6">
                  <div className="flex gap-3">
                    <Avatar>
                      <AvatarFallback>{post.avatar}</AvatarFallback>
                    </Avatar>
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        <span className="font-medium">{post.author}</span>
                        <span className="text-sm text-muted-foreground">{post.time}</span>
                      </div>
                      <p className="text-sm mb-4">{post.content}</p>
                      <div className="flex items-center gap-4">
                        <Button variant="ghost" size="sm" className="gap-1">
                          <Heart className="h-4 w-4" />
                          {post.likes}
                        </Button>
                        <Button variant="ghost" size="sm" className="gap-1">
                          <MessageCircle className="h-4 w-4" />
                          {post.comments}
                        </Button>
                        <Button variant="ghost" size="sm" className="gap-1">
                          <Share2 className="h-4 w-4" />
                          Share
                        </Button>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Trending Topics</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {trendingTopics.map((topic, index) => (
                    <Button key={index} variant="outline" size="sm">
                      #{topic}
                    </Button>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="text-lg">Frequently Asked</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <div className="text-sm">
                  <p className="font-medium">How to improve soil quality?</p>
                </div>
                <div className="text-sm">
                  <p className="font-medium">Best time to plant wheat?</p>
                </div>
                <div className="text-sm">
                  <p className="font-medium">Organic pest control methods?</p>
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

export default Forum;