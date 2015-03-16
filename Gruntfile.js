'use strict';

module.exports = function (grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        markdown: {
            readme: {
                files: {
                    'README.html': ['README.md']
                }
            },
            options: {
                template: 'template.html',
                autoTemplate: false,
                postCompile: function(src, context) {
                    return src.replace(/<pre>/g, '<pre class="prettyprint">');
                }
            }
        }
    });

    grunt.registerTask('default', [
        'markdown'
    ]);

    grunt.loadNpmTasks('grunt-markdown');

};