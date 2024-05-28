/*
* Point of this file is to handle the incoming request from the client
* After it handles the request, it will call the function to parse the resume
*/

import type { NextApiRequest, NextApiResponse } from 'next'
import { readPdf } from 'lib/parse-resume-from-pdf/read-pdf'
 
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'GET') {
    // Process a GET request
    res.status(200).json({ message: 'Hello from upload_CV! (Get)' })

  } else if (req.method === 'POST') {
    // Handle POST method
    res.status(200).json({ message: 'Hello from upload_CV! (Post)' })

    // Taken from /src/app/resume-parser/page.tsx
    readPdf(req.body)
      .then(textItems => {
        // Process the textItms returned by readPdf
        console.log(textItems)
      })
      .catch(error => {
        // Handle any errors that occurrred while reading the PDF
        console.error(error)
      })


    // Parse the incoming request containing the form data
    console.log(req.body)
  }
}


export const config = {
  api: {
    bodyParser: {
      sizeLimit: '10mb',
    },
  },
}