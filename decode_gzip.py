import base64
import gzip
from io import BytesIO
import urllib.parse

# Raw cookie value
cookie = "H4sIAAAAAAAA%2fzWPPU7DQBCFF0RSQcMJpkOi2PTQEH4iCkcKClJEOV6Pk8HrHbO7dmKQOA4VJ%2bAI3IU7sBahm%2fn09PS9zx81Cl6dW8w1msjigjZS1%2bJ0IM9o%2bRVzS3pa1OwWnsrw9vUxDqvv7FAdZeq4xE48R5qJFFGdZs%2fY4cSiW0%2bW0bNbX2bq5D%2fz0EqkF%2fWuDvawHei1SLWHo7ih%2bi%2bxa6Iab5kc%2baiu5j04rAk4wA16KwHm4qL0qOFJWqjYWiqg7qHEVOE1JNMGPUEUKJh0VIvHDcGKcpg2jWWDw1K4R1ORPwvpcEWePC7gloORjgZ1SBDudo0VjsO7JDMI9zCzuA1JT3zaSb9PDWuHQgEAAA%3d%3d"

try:
    # Step 1: URL Decode
    decoded_url = urllib.parse.unquote(cookie)

    # Step 2: Base64 Decode
    decoded_base64 = base64.b64decode(decoded_url)

    # Step 3: GZIP Decompress
    with gzip.GzipFile(fileobj=BytesIO(decoded_base64)) as gz:
        decompressed_data = gz.read()

    try:
        # Attempt to decode as UTF-8
        print(decompressed_data.decode('utf-8'))
    except UnicodeDecodeError:
        # If UTF-8 decoding fails, print raw binary
        print("Decompressed data is not UTF-8 encoded. Raw binary output:")
        print(decompressed_data)

except Exception as e:
    print(f"An error occurred: {e}")
