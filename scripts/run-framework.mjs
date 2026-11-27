import { spawn } from "node:child_process";

const mode = process.argv[2] ?? "dev";
const extraArgs = process.argv.slice(3);

if (!["dev", "build"].includes(mode)) {
  console.error(`Unsupported framework mode: ${mode}`);
  process.exit(1);
}

const command = process.platform === "win32" ? "pnpm.cmd" : "pnpm";
const child = spawn(command, ["exec", "vinext", mode, ...extraArgs], {
  stdio: "inherit",
  env: {
    ...process.env,
    NODE_ENV: mode === "build" ? "production" : "development",
  },
});

child.on("error", (error) => {
  console.error("Unable to start vinext:", error.message);
  process.exit(1);
});

child.on("exit", (code, signal) => {
  if (signal) {
    process.kill(process.pid, signal);
  } else {
    process.exit(code ?? 1);
  }
});
