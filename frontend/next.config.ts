import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // Configure Turbopack for better performance
  experimental: {
    turbopack: {},
  },
  // Set the root directory to avoid multiple lockfile warnings
  // This tells Next.js which package.json to consider as the root
};

export default nextConfig;
