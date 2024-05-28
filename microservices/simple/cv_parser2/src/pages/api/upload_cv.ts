import type { NextApiRequest, NextApiResponse } from 'next'
 
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'GET') {
    // Process a GET request
    res.status(200).json({ message: 'Hello from upload_CV! (Get)' })

  } else if (req.method === 'POST') {
    // Handle any other HTTP method
    res.status(200).json({ message: 'Hello from upload_CV! (Post)' })

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