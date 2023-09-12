#!/usr/bin/node

const fs = require('fs');

const fileAPath = 'fileA';
const fileBPath = 'fileB';

const fileAContent = fs.readFileSync(fileAPath, 'utf-8');
const fileBContent = fs.readFileSync(fileBPath, 'utf-8');
const concatenatedContent = fileAContent + fileBContent;

const concatenatedFilePath = 'fileC';

fs.writeFileSync(concatenatedFilePath, concatenatedContent, 'utf-8');
