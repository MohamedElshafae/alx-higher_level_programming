#!/usr/bin/node

const fs = require('fs');

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];

const fileAContent = fs.readFileSync(fileAPath, 'utf-8');
const fileBContent = fs.readFileSync(fileBPath, 'utf-8');
const concatenatedContent = fileAContent + fileBContent;

const concatenatedFilePath = process.argv[4];

fs.writeFileSync(concatenatedFilePath, concatenatedContent, 'utf-8');
