for i in {1..30}; do
  curl -s http://localhost:8085/health > /dev/null
  sleep 0.2
done
