/*
* Point of this file is to handle the incoming request from the client
* After it handles the request, it will call the function to parse the resume
*/

import type { NextApiRequest, NextApiResponse } from 'next'
import { readPdf } from 'lib/parse-resume-from-pdf/read-pdf'
import { groupTextItemsIntoLines } from 'lib/parse-resume-from-pdf/group-text-items-into-lines'
import { groupLinesIntoSections } from "lib/parse-resume-from-pdf/group-lines-into-sections";
import { extractResumeFromSections } from "lib/parse-resume-from-pdf/extract-resume-from-sections";
import path from 'path'
import formidable from 'formidable-serverless'
import { read } from 'fs'

const all = async (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method === 'GET') {
    // call the sharepoint microservice to get all the CVs
    try {
      const spCVs = await fetch('http://localhost:5001/sharepoint/cv/all')
      const filesToParse  = await spCVs.json()
      console.log(filesToParse["files"]);

      // Initialize an array to hold the parsed CVs
      const parsedCVs = [];

      // Process each retrieved file
      for (const file of filesToParse["files"]) {
        const parsedCV = await processFile(file["content"]);
        parsedCVs.push(parsedCV);
      }
      res.status(200).json(parsedCVs);
    } catch(err) {
      console.error(err);
      res.status(500).send(err);
    }
  } else {
    res.setHeader('Allow', ['POST'])
    res.status(405).end(`Method ${req.method} Not Allowed`)
  }
};

async function processFile(fileUrl: string) {
  // Step 1. Call the function to parse the resume
  const textItems = await readPdf(fileUrl);

  // Step 2. Group text items into lines
  const lines = groupTextItemsIntoLines(textItems);

  // Step 3. Group lines into sections
  const sections = groupLinesIntoSections(lines);

  // Step 4. Extract resume from sections
  const resume = extractResumeFromSections(sections);

  console.log(resume);

  return resume;
}

// Disable body parser to handle file upload
export const config = {
  api: {
    bodyParser: false
  }
}

export default all