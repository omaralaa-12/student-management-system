function SearchBar({
  search,
  setSearch,
  searchStudents,
}) {
  return (
    <div className="bg-white shadow rounded-lg p-6 mb-8">
      <div className="flex gap-4">

        <input
          type="text"
          placeholder="Search by name..."
          className="flex-1 border p-3 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <button
          onClick={searchStudents}
          className="bg-blue-600 hover:bg-blue-700 text-white px-6 rounded"
        >
          🔍 Search
        </button>

        <button
          onClick={() => {
            setSearch("");
            searchStudents("");
          }}
          className="bg-gray-500 hover:bg-gray-600 text-white px-6 rounded"
        >
          Reset
        </button>

      </div>
    </div>
  );
}

export default SearchBar;