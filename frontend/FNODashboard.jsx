
import React, { useEffect, useState } from "react";
import { Input } from "@/components/ui/input";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

export default function FNODashboard() {
  const [stocks, setStocks] = useState([]);
  const [search, setSearch] = useState("");

  const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/top-fno-picks";

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch(API_URL);
        const data = await res.json();
        setStocks(data);
      } catch (error) {
        console.error("Error fetching stock data:", error);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, [API_URL]);

  const filtered = stocks.filter(stock => stock.Stock.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">F&O Top Picks - Live Monitor</h1>
      <Input
        placeholder="Search stock (e.g., HDFCBANK)"
        value={search}
        onChange={e => setSearch(e.target.value)}
        className="mb-4"
      />
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Stock</TableHead>
            <TableHead>Price Change %</TableHead>
            <TableHead>Volume Change %</TableHead>
            <TableHead>OI Trend</TableHead>
            <TableHead>PCR</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {filtered.map((stock, idx) => (
            <TableRow key={idx}>
              <TableCell>{stock.Stock}</TableCell>
              <TableCell>{stock["Price Change (%)"]}</TableCell>
              <TableCell>{stock["Volume Change (%)"]}</TableCell>
              <TableCell>{stock["OI Trend"]}</TableCell>
              <TableCell>{stock.PCR}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
