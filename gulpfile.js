var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-clean-css');
var rename = require('gulp-rename');
var sourcemap = require('gulp-sourcemaps');
var livereload = require('gulp-livereload');

gulp.task('sass', function() {
    return gulp.src('flace/static/css/scss/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('static/stylesheets'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('static/stylesheets'))
        .pipe(livereload());
});

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('scss/*.scss', ['sass']);

    /* Trigger a live reload on any Django template changes */
    gulp.watch('**/templates/*').on('change', livereload.changed);

});

gulp.task('default', ['sass', 'watch']);