/** POST /api/data */

export default function handler(req, res) {
    const { method, body } = req;

    console.log("Received request:", method, body);

    if (method === 'POST') {
        // Process the POST request data here
        console.log("Processing data:", body);

        return res.status(201).json({ message: 'Data received successfully', data: body });
    }
    else {
        return res.status(405).json({ message: 'Method Not Allowed' }); // Method Not Allowed
    }



};