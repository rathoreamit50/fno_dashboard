import React, { useEffect, useState } from "react";

export default function FNODashboard() {
  const [stocks, setStocks] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("http://localhost:8000/api/top-fno-picks");
        const data = await res.json();
        setStocks(data);
      } catch (error) {
        console.error("Error fetching stock data:", error);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  const filtered = stocks.filter((stock) =>
    stock.Stock.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>F&O Live Monitor</h1>
      <input
        placeholder="Search stock"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{ marginBottom: 10, padding: 5, width: "100%", maxWidth: 300 }}
      />
      <table
        border="1"
        cellPadding="8"
        cellSpacing="0"
        style={{ width: "100%", borderCollapse: "collapse" }}
      >
        <thead style={{ backgroundColor: "#f4f4f4" }}>
          <tr>
            <th>Stock</th>
            <th>Price Change (%)</th>
            <th>Volume Change (%)</th>
            <th>OI Trend</th>
            <th>PCR</th>
          </tr>
        </thead>
        <tbody>
          {filtered.length > 0 ? (
            filtered.map((stock, idx) => (
              <tr key={idx}>
                <td>{stock?.Stock || "—"}</td>
                <td>{stock?.["Price Change (%)"] ?? "—"}</td>
                <td>{stock?.["Volume Change (%)"] ?? "—"}</td>
                <td>{stock?.["OI Trend"] ?? "—"}</td>
                <td>{stock?.PCR ?? "—"}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5" style={{ textAlign: "center" }}>
                No data available.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
