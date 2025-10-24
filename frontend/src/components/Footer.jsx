import { Link } from "react-router-dom";
import { Sprout } from "lucide-react";

const Footer = () => {
  return (
    <footer className="bg-muted border-t border-border mt-12">
      <div className="container mx-auto px-4 py-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2 text-primary">
            <Sprout className="h-6 w-6" />
            <span className="font-bold">AgriAssist</span>
          </div>
          
          <div className="flex flex-wrap items-center justify-center gap-6 text-sm">
            <Link to="/contact" className="text-muted-foreground hover:text-primary transition-colors">
              Contact
            </Link>
            <Link to="/about" className="text-muted-foreground hover:text-primary transition-colors">
              About Us
            </Link>
            <Link to="/help" className="text-muted-foreground hover:text-primary transition-colors">
              Help
            </Link>
            <Link to="/privacy" className="text-muted-foreground hover:text-primary transition-colors">
              Privacy Policy
            </Link>
          </div>
          
          <div className="text-sm text-muted-foreground">
            © 2025 AgriAssist. All rights reserved.
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
