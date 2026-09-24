// ESLint 9 dùng "flat config" — cấu hình là một mảng các khối luật.
module.exports = [
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: 'commonjs',
      // Khai báo các biến toàn cục của Node để ESLint không báo "không tồn tại"
      globals: {
        require: 'readonly',
        module: 'writable',
        process: 'readonly',
        console: 'readonly',
        __dirname: 'readonly',
      },
    },
    rules: {
      'no-unused-vars': 'error',   // biến khai rồi không dùng → lỗi
      'no-undef': 'error',         // dùng tên không tồn tại → lỗi
      'eqeqeq': 'error',           // bắt buộc === thay vì == (tránh bẫy so sánh lỏng)
      'no-console': 'off',         // app nhỏ, cho phép console.log
    },
  },
];
