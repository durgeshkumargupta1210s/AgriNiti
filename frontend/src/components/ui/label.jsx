import * as React from "react";
import * as LabelPrimitive from "@radix-ui/react-label";
// 'type VariantProps' has been removed from this import
import { cva } from "class-variance-authority";

import { cn } from "@/lib/utils";

const labelVariants = cva(
  "text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
);

// All TypeScript types have been removed from this line
const Label = React.forwardRef(({ className, ...props }, ref) => (
  // The <LabelPrimitive.Root> has been added back
  <LabelPrimitive.Root
    ref={ref}
    className={cn(labelVariants(), className)}
    {...props}
  />
));
Label.displayName = LabelPrimitive.Root.displayName;

export { Label };