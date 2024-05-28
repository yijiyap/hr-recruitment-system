import type { NextApiRequest, NextApiResponse } from "next";
import { parse } from "url";
import { parseResumeFromPdf } from "lib/parse-resume-from-pdf";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest, res: NextApiResponse) {
    const jsonBody = await req.json();
    const { fileUrl } = jsonBody;
    const resume = await parseResumeFromPdf(fileUrl);
    res.json(resume);
    return NextResponse.json(resume);
}

export function GET(req: NextRequest, res: NextApiResponse) {
    res.status(405).json({ error: "Method Not Allowed" });
    return NextResponse.json({ error: "Method Not Allowed" });
}
