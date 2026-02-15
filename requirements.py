<!DOCTYPE html>
<html>
<head>
    <title>Mashup Generator</title>
    <style>
        body { font-family: sans-serif; background: #f4f7f6; display: flex; justify-content: center; padding-top: 50px; }
        .card { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 400px; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background: #a55d5d; color: white; border: none; border-radius: 6px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2 style="text-align: center;">Mashup Generator</h2>
        <form action="/process" method="POST">
            <input type="text" name="singer" placeholder="Singer Name" required>
            <input type="number" name="n" placeholder="Number of Videos (N > 10)" required>
            <input type="number" name="y" placeholder="Duration per song (seconds > 20)" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <button type="submit">Generate Mashup</button>
        </form>
    </div>
</body>
</html>
