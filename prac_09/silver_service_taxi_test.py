from silver_service_taxi import SilverServiceTaxi

sst = SilverServiceTaxi("taxi", 1000, 2)
sst.start_fare()
sst.drive(18)
print(f"${sst.get_fare():.2f}")
print(sst)
