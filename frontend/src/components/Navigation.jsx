import { Link, useLocation, useNavigate } from "react-router-dom";
import { Globe, Bell, Sprout, LogIn, LogOut } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { useState } from "react";

const Navigation = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [isLoggedIn, setIsLoggedIn] = useState(false); // Track login state (should be from context/state management)
  
  const navItems = [
    { path: "/dashboard", label: "Home" },
    { path: "/crop-advisory", label: "Crop Advisory" },
    { path: "/weather-market", label: "Weather & Market" },
    { path: "/forum", label: "Forum" },
    { path: "/profile", label: "Profile" },
  ];

  const isActive = (path) => location.pathname === path;

  const handleLogout = () => {
    setIsLoggedIn(false);
    navigate('/');
  };

  return (
    <nav className="sticky top-0 z-50 bg-card border-b border-border shadow-sm">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/dashboard" className="flex items-center gap-2 text-primary font-bold text-xl">
            <Sprout className="h-8 w-8" />
            <span className="hidden sm:inline">Smart Krishi</span>
          </Link>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center gap-6">
            {navItems.map((item) => (
              <Link
                key={item.path}
                to={item.path}
                className={`text-sm font-medium transition-colors hover:text-primary ${
                  isActive(item.path) ? "text-primary" : "text-muted-foreground"
                }`}
              >
                {item.label}
              </Link>
            ))}
          </div>

          {/* Right Section */}
          <div className="flex items-center gap-3">
            <Button variant="ghost" size="icon" className="relative">
              <Bell className="h-5 w-5" />
              <span className="absolute top-1 right-1 h-2 w-2 bg-accent rounded-full"></span>
            </Button>
            <Button variant="outline" size="sm" className="gap-2">
              <Globe className="h-4 w-4" />
              <span className="hidden sm:inline">EN</span>
            </Button>

            {isLoggedIn ? (
              <div className="hidden md:flex items-center gap-2">
                <Avatar className="h-8 w-8 cursor-pointer" onClick={() => navigate('/profile')}>
                  <AvatarFallback className="bg-primary text-primary-foreground text-sm">
                    RK
                  </AvatarFallback>
                </Avatar>
                <Button 
                  variant="ghost" 
                  size="sm"
                  onClick={handleLogout}
                  className="gap-1"
                >
                  <LogOut className="h-4 w-4" />
                  <span className="hidden lg:inline">Logout</span>
                </Button>
              </div>
            ) : (
              <Button 
                variant="default" 
                size="sm"
                onClick={() => navigate('/login')}
                className="gap-2 hidden md:flex"
              >
                <LogIn className="h-4 w-4" />
                Login
              </Button>
            )}
          </div>
        </div>
      </div>

      {/* Mobile Navigation */}
      <div className="md:hidden border-t border-border">
        <div className="flex justify-around py-2">
          {navItems.slice(0, 5).map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`text-xs font-medium px-2 py-1 rounded transition-colors ${
                isActive(item.path) 
                  ? "bg-primary text-primary-foreground" 
                  : "text-muted-foreground hover:text-primary"
              }`}
            >
              {item.label.split(' ')[0]}
            </Link>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
