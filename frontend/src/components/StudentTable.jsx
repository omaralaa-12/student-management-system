function StudentTable({
  students,
  deleteStudent,
  editStudent,
}) {
  return (
    <div className="bg-white shadow rounded-lg overflow-hidden">
      <table className="w-full">

        <thead className="bg-blue-600 text-white">
          <tr>
            <th className="p-4 text-left">ID</th>
            <th className="p-4 text-left">Name</th>
            <th className="p-4 text-left">Age</th>
            <th className="p-4 text-left">Major</th>
            <th className="p-4 text-center">Actions</th>
          </tr>
        </thead>

        <tbody>

          {students.map((student) => (

            <tr
              key={student.id}
              className="border-b hover:bg-gray-100 transition"
            >

              <td className="p-4">{student.id}</td>

              <td className="p-4 font-semibold">
                {student.name}
              </td>

              <td className="p-4">
                {student.age}
              </td>

              <td className="p-4">
                {student.major}
              </td>

              <td className="p-4 text-center">

                <button
                  onClick={() => editStudent(student)}
                  className="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded mr-2 transition"
                >
                  ✏️ Edit
                </button>

                <button
                  onClick={() => deleteStudent(student.id)}
                  className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded transition"
                >
                  🗑 Delete
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>
    </div>
  );
}

export default StudentTable;