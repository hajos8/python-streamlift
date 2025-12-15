/** POST /api/data */

export default function handler(req, res) {
    const { method, body } = req;

    console.log("Received request:", method, body);

    return res.sendStatus(201);

};