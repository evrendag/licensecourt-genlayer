import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "LICENSECOURT — Evidence for every release",
  description: "Version-pinned open-source license compatibility passports finalized through GenLayer consensus.",
  icons: { icon: "/favicon.svg", shortcut: "/favicon.svg" },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body className="antialiased">{children}</body></html>;
}
