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

const uploadfile = async (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method === 'POST') {
    return uploadfilePOST(req, res)
  } else {
    res.setHeader('Allow', ['POST'])
    res.status(405).end(`Method ${req.method} Not Allowed`)
  }
};

async function uploadfilePOST (req: NextApiRequest, res: NextApiResponse) {
  const form = new formidable.IncomingForm()
  form.uploadDir = path.join(process.cwd(), 'uploads')
  form.keepExtensions = true
  form.parse(req, (err, fields, files) => {
    if (err) {
      res.status(500).send(err);
      return;
    }

    // Iterate over the keys of the files object to find the uploaded file(s)
    Object.keys(files).forEach(async (fileName) => {
      const fileUrl = files[fileName].path

      // Step 1. Call the function to parse the resume
      const textItems = await readPdf(fileUrl);

      // Step 2. Group text items into lines
      const lines = groupTextItemsIntoLines(textItems);

      // Step 3. Group lines into sections
      const sections = groupLinesIntoSections(lines);

      // Step 4. Extract resume from sections
      const resume = extractResumeFromSections(sections);

      console.log(resume);

      // Send the resume back to another endpoint


    });
    res.status(200).json({ fields, files })
  })
}

// Disable body parser to handle file upload
export const config = {
  api: {
    bodyParser: false
  }
}

export default uploadfile