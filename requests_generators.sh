for i in {1..300}; do
  echo "sending request $i"
  curl -s http://localhost:8085/health > /dev/null
  sleep 0.2
done
