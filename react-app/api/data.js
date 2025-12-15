/** POST /api/data */

export default function handler(req, res) {
    const { method, body } = req;

    console.log("Received request:", method, body);

    if (method === 'POST') {
        // Process the POST request data here
        console.log("Processing data:", body);

        return res.sendStatus(201);
    }
    else {
        return res.sendStatus(405); // Method Not Allowed
    }



};