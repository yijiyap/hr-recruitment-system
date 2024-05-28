/*
* Point of this file is to handle the incoming request from the client
* After it handles the request, it will call the function to parse the resume
*/

import type { NextApiRequest, NextApiResponse } from 'next'
import { readPdf } from 'lib/parse-resume-from-pdf/read-pdf'
import path from 'path'
import formidable from 'formidable-serverless'

const uploadfile = async (req: NextApiRequest, res: NextApiResponse) => {
  if (req.method === 'POST') {
    return uploadfilePOST(req, res)
  } else {
    res.setHeader('Allow', ['POST'])
    res.status(405).end(`Method ${req.method} Not Allowed`)
  }

  async function uploadfilePOST (req, res) {
    const form = new formidable.IncomingForm()
    form.uploadDir = path.join(process.cwd(), 'uploads')
    form.keepExtensions = true
    form.parse(req, (err, fields, files) => {
      if (err) res.status(500).send(err)
      res.status(200).json({ fields, files })
    })
  }
}

export const config = {
  api: {
    bodyParser: false
  }
}

export default uploadfile