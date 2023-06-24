#!/usr/bin/env node
import select from "@inquirer/select";
import chalk from "chalk";
import { spawn } from "child_process";
import { readFile } from "fs/promises";

const inventory = await readFile(new URL("./inventory.json", import.meta.url));

const sketches = JSON.parse(inventory);

const answer = await select({
  message: "Select sketch:",
  choices: Object.entries(sketches).map(([key, label]) => ({
    name: label,
    value: key,
  })),
});

const sketchFile = `${answer}.py`;
const feedback = `Running sketch: ${chalk.green(
  sketches[answer]
)} (${sketchFile})`;
console.log(feedback);

const childProcess = spawn(`python ./sketches/${sketchFile}`, { shell: true });
childProcess.on("exit", () => console.log(chalk.blue("Sketch closed, bye!")));
