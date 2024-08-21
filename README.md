from uuid_with_datetime.generator import generate_uuid_with_datetime

# Generate UUID with 24-hour format
print(generate_uuid_with_datetime(format_24h=True))

# Generate UUID with 12-hour format
print(generate_uuid_with_datetime(format_24h=False))
