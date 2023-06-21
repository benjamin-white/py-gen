#!/usr/bin/env node
import inquirer from "inquirer";
import chalk from "chalk";
import { spawn } from "child_process";

// fix the npm log level
// load options from config file
// remove main inquirere

const sketches = {
  main: "Main",
  notMain: "Do Not Choose",
};

import select from "@inquirer/select";

const answer = await select({
  message: "Select sketch:",
  choices: Object.entries(sketches).map(([key, label]) => ({
    name: label,
    value: key,
  })),
});

// const sketchFile = `${answer}.py`;
// const feedback = `Running sketch: ${chalk.green(
//   sketches[answer]
// )} (${sketchFile})`;

// console.log(feedback);
// spawn("python", [sketchFile]);
